from django.urls import path
from book.views import set_session, get_session, test
from book.views import JdLonginView,CenterView

urlpatterns = [
   path('set_session/',set_session),
   path('get_session/',get_session),
   path('test/',test),
   # TODO 类视图的url
   path('login/',JdLonginView.as_view()),
   path('center/',CenterView.as_view()),
]