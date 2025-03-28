from flask import Flask, render_template, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime, timedelta
import csv
import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg before importing pyplot
import matplotlib.pyplot as plt
import io
import base64

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sales.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Sales model with product, price, and date_sold
class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date_sold = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Sales {self.product}>'

# ---- Helper Functions ----

# Function to insert dummy data
def insert_dummy_data():
    with app.app_context():
        db.drop_all()
        db.create_all()

        products = {
            'Laptop': 1000.00,
            'Smartphone': 700.00,
            'Headphones': 150.00,
            'Smartwatch': 200.00,
            'Tablet': 300.00
        }

        for _ in range(50):
            product = random.choice(list(products.keys()))
            price = products[product]
            sales = random.randint(1, 10)
            total_price = price * sales
            random_days = random.randint(1, 365)
            date = datetime.now() - timedelta(days=random_days)
            formatted_date = date.strftime('%Y-%m-%d')

            sale = Sales(product=product, price=total_price, date_sold=formatted_date)
            db.session.add(sale)

        db.session.commit()

# Call the function to insert dummy data
insert_dummy_data()

# ---- Flask Routes ----

@app.route('/')
def index():
    return render_template('bar_chart.html')

@app.route('/pie')
def pie_chart():
    return render_template('pie_chart.html')

@app.route('/histogram')
def histogram_chart():
    return render_template('histogram.html')

@app.route('/data')
def get_data():
    sales_data = Sales.query.all()
    data = [{"product": sale.product, "price": sale.price, "date_sold": sale.date_sold} for sale in sales_data]
    return jsonify(data)

@app.route('/download')
def download_csv():
    sales_data = Sales.query.all()

    csv_data = "Product,Price,Date Sold\n"
    for sale in sales_data:
        csv_data += f"{sale.product},{sale.price},{sale.date_sold}\n"

    response = Response(csv_data, content_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=sales_data.csv"
    return response

@app.route('/matplotlib_chart_image')
def matplotlib_chart():
    try:
        sales_data = Sales.query.all()

        earnings_by_product = {}
        for sale in sales_data:
            if sale.product not in earnings_by_product:
                earnings_by_product[sale.product] = 0
            earnings_by_product[sale.product] += sale.price

        products = list(earnings_by_product.keys())
        earnings = list(earnings_by_product.values())

        # Create a Matplotlib figure
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(products, earnings, color='skyblue')
        ax.set_xlabel("Product")
        ax.set_ylabel("Total Earnings ($)")
        ax.set_title("Earnings by Product")
        plt.xticks(rotation=45)
        plt.tight_layout(pad=2.0)

        img_buffer = io.BytesIO()
        fig.savefig(img_buffer, format='png', bbox_inches='tight')
        img_buffer.seek(0)
        
        # Explicitly close the figure
        plt.close(fig)
        
        return Response(img_buffer.getvalue(), mimetype='image/png')
    except Exception as e:
        print(f"Error generating matplotlib chart: {e}")
        return Response(status=500)

# ---- Main Application Runner ----

if __name__ == '__main__':
    app.run(debug=True)
