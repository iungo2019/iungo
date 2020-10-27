from django.urls import path
from .views import MembershipSelectView, PaymentView, updateTransactions, SubscriptionView, CancelSubscription

app_name = 'memberships'

urlpatterns = [
    path('select', MembershipSelectView.as_view(), name='select'),
    path('payment/', PaymentView, name='payment'),
    path('update-transactions/<subscription_id>/', updateTransactions, name='update-transactions'),
    path('subscription/', SubscriptionView, name='subscription'),
    path('cancel/', CancelSubscription, name='cancel'),

]
