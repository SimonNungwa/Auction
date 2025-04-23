from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

# @routes.route('/')
# def index():
#     return render_template('index.html')

@routes.route('/')
def home():
    categories = [
        {
            'name': 'Art & Antiques',
            # 'items': AuctionItem.query.filter_by(category='art').limit(3).all()
        },
        {
            'name': 'Jewelry & Watches',
            # 'items': AuctionItem.query.filter_by(category='jewelry').limit(3).all()
        },
        {
            'name': 'Ending Soon',
            # 'items': AuctionItem.query.filter(AuctionItem.end_time <= some_time_threshold).limit(3).all()
        }
    ]
    return render_template('index.html', categories=categories)


@routes.route('/about')
def about():
    return render_template('about.html')

@routes.route('/recover')
def recover():
    return render_template('recover.html')

@routes.route('/login')
def login():
    return render_template('login.html')

@routes.route('/signup')
def signup():
    return render_template('signup.html')

@routes.route('/search')
def search():
    return render_template('searchPage.html')

@routes.route('/services')
def services():
    return render_template('services.html')
