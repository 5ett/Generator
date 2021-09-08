import string
from recapp.tryts import generate_id, greeting_tag
from recapp import app, db, crypt
from recapp.models import User, Ticket, Storage
from recapp.forms import Login, Generator, Search, Head
from flask import redirect, url_for, render_template, flash
from flask_login import current_user, login_user, logout_user, login_required


@app.route("/", methods=['GET', 'POST'])
def index():
    time_now = greeting_tag()
    form = Login()
    if form.validate_on_submit():
        try:
            user_valid = User.query.filter_by(
                username=form.username.data).first()
        except:
            user_valid = User.query.filter_by(name=form.username.data).first()
        else:
            flash('Wrong credentials', 'danger')

        # pass_auth = crypt.check_password_hash(
        #     user_valid.password, form.password.data)
        if user_valid and crypt.check_password_hash(user_valid.password, form.password.data):
            login_user(user_valid)
        else:
            flash('Wrong credentials', 'danger')

    recent_forms = Ticket.query.order_by(Ticket.id.desc()).all()

    return render_template('index.html', form=form, recent_forms=recent_forms, time=time_now)


@app.route("/add_head/<string:ticket_type>", methods=['GET', 'POST'])
@login_required
def add_head(ticket_type):

    keys = {'quote': 'PRO', 'receipt': 'REC'}
    form = Head()
    if form.validate_on_submit():
        generated_pseudo_id = generate_id(keys[ticket_type])
        name_to_save = string.capwords(form.name.data)

        create_ticket = Ticket(pseudo_id=generated_pseudo_id, belongs_to=name_to_save,
                               form_type=keys[ticket_type], status='draft', total_sum=0)
        db.session.add(create_ticket)
        db.session.commit()

        ticket = Ticket.query.filter_by(pseudo_id=generated_pseudo_id).first()
        # return redirect(url_for(f'make_{ticket_type}', ticket_pseudo_id=generated_pseudo_id))
        return redirect(url_for('form_viewer', ticket_id=ticket.id))

    return render_template('add_head.html', form=form, ticket_type=ticket_type, title='Add Head')


@app.route("/all_forms", methods=['GET', 'POST'])
@login_required
def all_forms():
    if not current_user.is_authenticated:
        flash('you need to login before accessing this page', 'danger')
        return redirect(url_for('index'))

    form = Search()
    if form.validate_on_submit():
        payload = []
        try:
            search_param = form.search_bar.data.split(':')
            if search_param[0] == 'quantity':
                search_input = int(search_param[1])
                return_query = Storage.query.filter_by(
                    item_quantity=search_input).order_by(Storage.id.desc()).all()

            elif search_param[0] == 'price':
                search_input = float(search_param[1])

                return_query_batch = Ticket.query.filter_by(
                    total_sum=search_input).order_by(Ticket.id.desc()).all()
                if return_query_batch:
                    payload.append(return_query_batch)

                return_query_individual = Storage.query.filter_by(
                    total_price=search_input).order_by(Storage.id.desc()).all()
                if return_query_individual:
                    payload.append(return_query_batch)
        except:
            return_query = Ticket.query.filter_by(
                belongs_to=form.search_bar.data).order_by(Ticket.id.desc()).all()

    view_all_forms = Ticket.query.order_by(Ticket.id.desc()).all()
    return render_template('all_forms.html', form=form, viewer=view_all_forms, title='Records')


@app.route("/form_viewer/<int:ticket_id>", methods=['GET', 'POST'])
def form_viewer(ticket_id):
    call_for_view = Ticket.query.filter_by(id=ticket_id).first()

    form = Generator()
    if form.validate_on_submit():
        entered_item_name = string.capwords(form.item_name.data)
        ref_item_qtty = form.item_quantity.data
        ref_unit_price = form.unit_price.data
        ref_total_price = ref_unit_price * ref_item_qtty
        ref_total_price = round(ref_total_price, 2)

        new_form_item = Storage(item_name=entered_item_name, item_quantity=ref_item_qtty,
                                unit_price=ref_unit_price, total_price=ref_total_price, ticket_link=call_for_view.id)

        call_for_view.subtotal = round(
            (call_for_view.subtotal + ref_total_price), 2)
        call_for_view.vat = round((0.04 * call_for_view.subtotal), 2)
        call_for_view.total_sum = round(
            (call_for_view.subtotal + call_for_view.vat), 2)
        call_for_view.no_items += 1

        db.session.add(new_form_item)
        db.session.commit()

    resources = Storage.query.filter_by(
        ticket_link=ticket_id).all()

    return render_template('viewer.html', viewer=call_for_view, title=f'{call_for_view.pseudo_id}', resources=resources, form=form, count=0)


@app.route("/complete_form/<string:ticket_pseudo_id>", methods=['GET', 'POST'])
def complete_form(ticket_pseudo_id):
    main_ticket = Ticket.query.filter_by(pseudo_id=ticket_pseudo_id).first()
    if main_ticket:
        resources = Storage.query.filter_by(ticket_link=main_ticket.id).all()
    return render_template('final_print.html', resources=resources, title=main_ticket.belongs_to, viewer=main_ticket)


@app.route("/delete_form/<string:ticket_pseudo_id>", methods=['GET', 'POST'])
def delete_form(ticket_pseudo_id):
    to_delete_main = Ticket.query.filter_by(pseudo_id=ticket_pseudo_id).first()
    if to_delete_main:
        to_delete_sub = Storage.query.filter_by(
            ticket_link=to_delete_main.id).all()
        for item in to_delete_sub:
            db.session.delete(item)

    db.session.delete(to_delete_main)
    db.session.commit()

    return redirect(url_for('index'))


@app.route("/delete_item/<int:item_id>", methods=['GET', 'POST'])
def delete_item(item_id):
    to_delete_item = Storage.query.get_or_404(item_id)
    if to_delete_item:
        source = Ticket.query.get_or_404(to_delete_item.ticket_link)
        source.subtotal = source.subtotal - to_delete_item.total_price
        source.vat = round((0.04 * source.subtotal), 2)
        source.total_sum = round((source.subtotal + source.vat), 2)
        source.no_items -= 1

        db.session.delete(to_delete_item)
    db.session.commit()

    return redirect(url_for('form_viewer', ticket_id=source.id))


@app.route("/draftify/<string:ticket_pseudo_id>", methods=['GET', 'POST'])
def draftify(ticket_pseudo_id):
    keys = {'PRO': 'quotation', 'REC': 'receipt'}
    new_query = Ticket.query.filter_by(pseudo_id=ticket_pseudo_id).first()
    new_query.status = 'draft'
    db.session.commit()

    return redirect(url_for(f'make_{keys[new_query.ticket_type]}'))


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
