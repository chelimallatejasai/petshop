from django.shortcuts import render

def home(request):
    # Sample data for demonstration
    featured_products = [
        {'id': 1, 'name': 'Premium Dog Food', 'price': 29.99, 'image': 'dog-food.jpg'},
        {'id': 2, 'name': 'Cat Toy Set', 'price': 15.99, 'image': 'cat-toys.jpg'},
        {'id': 3, 'name': 'Bird Cage', 'price': 89.99, 'image': 'bird-cage.jpg'},
    ]
    return render(request, 'pet/home.html', {'featured_products': featured_products})

def product_list(request):
    products = [
        {'id': 1, 'name': 'Premium Dog Food', 'price': 29.99, 'category': 'Food', 'image': 'dog-food.jpg'},
        {'id': 2, 'name': 'Cat Toy Set', 'price': 15.99, 'category': 'Toys', 'image': 'cat-toys.jpg'},
        {'id': 3, 'name': 'Bird Cage', 'price': 89.99, 'category': 'Housing', 'image': 'bird-cage.jpg'},
        {'id': 4, 'name': 'Fish Tank', 'price': 149.99, 'category': 'Housing', 'image': 'fish-tank.jpg'},
        {'id': 5, 'name': 'Dog Leash', 'price': 19.99, 'category': 'Accessories', 'image': 'dog-leash.jpg'},
        {'id': 6, 'name': 'Cat Litter', 'price': 12.99, 'category': 'Care', 'image': 'cat-litter.jpg'},
    ]
    return render(request, 'pet/product_list.html', {'products': products})

def product_detail(request, product_id):
    # Sample product data
    product = {
        'id': product_id,
        'name': 'Premium Dog Food',
        'price': 29.99,
        'description': 'High-quality nutrition for your beloved dog. Made with real meat and wholesome ingredients.',
        'features': ['High protein content', 'No artificial preservatives', 'Supports healthy digestion', 'Suitable for all breeds'],
        'image': 'dog-food.jpg',
        'category': 'Food'
    }
    return render(request, 'pet/product_detail.html', {'product': product})

def checkout(request):
    # Sample cart data
    cart_items = [
        {'name': 'Premium Dog Food', 'price': 29.99, 'quantity': 2},
        {'name': 'Cat Toy Set', 'price': 15.99, 'quantity': 1},
    ]
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return render(request, 'pet/checkout.html', {'cart_items': cart_items, 'total': total})

def contact(request):
    return render(request, 'pet/contact.html')
