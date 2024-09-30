import numpy as np
from django import forms
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, ContactForm, RiskCalculatorForm
from django.contrib import messages
import logging
logger = logging.getLogger(__name__)

@login_required
def your_view(request):
    # Your view logic
    return render(request, 'chiliza/Chiliza.html')

# Registration Form
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            messages.success(request, 'Your account has been created successfully! You can now log in.')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            print(form.errors) # Print any validation errors
    else:
        form = RegistrationForm()

    return render(request, 'Chiliza/register.html', {'form': form})

# Login Form
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # This fetches the authenticated user directly
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')  # Redirect to home or another page
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'Chiliza/login.html', {'form': form})

# Home Page
@login_required
def home(request):
    home_image = 'home/home_image.jpg'  # Path to the Agricultural Economics image
    home_image2 = 'home/home_image1.jpg'  # Path to the Agribusiness image

    about_content = {
        "mission": "Our mission is to provide comprehensive advisory services that help farmers, agribusinesses, and policymakers make informed decisions.",
        "vision": "We envision a future where agriculture thrives through innovation, sustainability, and strategic decision-making.",
        "why_choose": [
            "Expertise in Agricultural Economics: Our team of agricultural economists and analysts brings extensive knowledge of global agricultural markets and trends.",
            "Data-Driven Insights: We use the latest data analytics and market research to provide insights that drive growth and efficiency.",
            "Sustainability Focus: We are committed to helping our clients adopt sustainable farming practices that reduce environmental impact and improve resource management.",
            "Tailored Solutions: We understand that each client’s needs are unique, and we work closely with them to develop solutions that fit their specific goals and challenges.",
            "Industry Relationships: Our extensive network within the agricultural industry enables us to provide the latest regulatory updates, market intelligence, and best practices.",
        ],
    }

    # Split the reasons into tuples (before and after the colon)
    about_content["why_choose"] = [(reason.split(':')[0].strip(), reason.split(':')[1].strip()) for reason in about_content['why_choose']]

    return render(request, 'Chiliza/home.html', {'home_image': home_image, 'home_image2': home_image2, 'about_content': about_content})

# Contact Form
@login_required
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # Process the form data here
        try:
            send_mail(
                form.cleaned_data['name'],
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                ['qj0q3@example.com'],
                fail_silently=False
            )
            messages.success(request, 'Thank you for contacting us!')
            form = ContactForm()  # Reset the form after successful submission
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later.')

    return render(request, 'Chiliza/contact.html', {'form': form})

# Services
@login_required
def services(request):
    services = [
        {
            'image': 'services/market_research.jpg',
            'title': 'Market Research & Analysis',
            'snippet': 'Our team provides detailed market analysis, giving farmers the best market recommendations.',
        },
        {
            'image': 'services/sustainability.jpg',
            'title': 'Sustainability & Resource Management',
            'snippet': 'We help farmers implement sustainable farming practices.',
        },
        {
            'image': 'services/financial_planning.jpg',
            'title': 'Farm Financial Planning and Risk Management',
            'snippet': 'Our experts assist in budgeting, financial planning, and risk management.',
        },
        {
            'image': 'services/gallery_image.jpg',  # Use media path for gallery images
            'title': 'Farmer at the Fresh Produce Market',
            'snippet': 'Farmers buying at the fresh produce market',
        },
        {
            'image': 'services/market_interaction.jpg',
            'title': 'Agricultural Market',
            'snippet': 'Agricultural Market interactions',
        },
        {
            'image': 'services/financial_projections.jpg',
            'title': 'Financial Projections',
            'snippet': 'Financial Projections after numerous farming seasons',
        },
    ]

    context = {'services': services}
    return render(request, 'Chiliza/services.html', context)

# Risk Calculator
def calculate_volatility(prices):
    # Check if prices are provided
    if not prices or ',' not in prices:
        return 0.0  # Return 0% if no prices are given

    prices_list = [float(price) for price in prices.split(',') if price]  # Convert string to list of floats

    # Check if we have at least two prices for volatility calculation
    if len(prices_list) < 2:
        return 0.0  # Return 0% if not enough data

    price_changes = np.diff(prices_list) / prices_list[:-1]  # Calculate percentage changes
    volatility = np.std(price_changes) * 100  # Convert to percentage
    return volatility

@login_required  # This will ensure the user is logged in before accessing this view
def risk_calculator(request):
    risk_percentage = None  # Initialize risk_percentage
    market_volatility = None  # Initialize market_volatility

    if request.method == 'POST':
        form = RiskCalculatorForm(request.POST)
        if form.is_valid():
            # Extract form data
            crop_type = form.cleaned_data['crop_type']
            farm_size = form.cleaned_data['farm_size']
            expected_yield = form.cleaned_data['expected_yield']
            weather_risk = form.cleaned_data['weather_risk']
            financial_stability = form.cleaned_data['financial_stability']
            pest_prevalence = form.cleaned_data['pest_prevalence']
            historical_prices = form.cleaned_data['historical_prices']

            # Sample calculation logic
            risk_score = 0
            if weather_risk == 'high':
                risk_score += 30
            elif weather_risk == 'moderate':
                risk_score += 15

            if financial_stability == 'high-risk':
                risk_score += 30
            elif financial_stability == 'uncertain':
                risk_score += 20

            if pest_prevalence == 'high':
                risk_score += 25
            elif pest_prevalence == 'moderate':
                risk_score += 15

            # Calculate market volatility
            market_volatility = calculate_volatility(historical_prices)
            risk_score += min(market_volatility, 30)  # Cap volatility contribution at 30%

            # Calculate total risk score
            risk_percentage = min(risk_score, 100)  # Risk is out of 100%

    else:
        form = RiskCalculatorForm()

    return render(request, 'Chiliza/risk_calculator.html', {
        'form': form,
        'risk_percentage': risk_percentage,
        'market_volatility': market_volatility,
    })