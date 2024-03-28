from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from photosessionapp.forms import ReservationCreateForm
from photosessionapp.models import Photographer, CustomUser, Review, Reservation


def root_view(request):
    user = CustomUser
    return render(request, 'root.html', {'user': user})


class MainView(ListView):
    model = Photographer
    template_name = 'photosession/main.html'
    context_object_name = 'photographer'

    def get_context_data(self, *, object_list=None, **kwargs):
        photographers = Photographer.objects.all()[:3]
        return {'photographer': photographers}

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.get_context_data())


class PhotographerListView(ListView):
    paginate_by = 3
    model = Photographer
    context_object_name = 'photographer'
    template_name = 'photosession/photographer.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(PhotographerListView, self).get_context_data()
    #
    # def get(self, request, *args, **kwargs):
    #     return render(self.request, self.template_name, self.get_context_data())

class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationCreateForm
    template_name = 'photosession/reservationform.html'
    context_object_name = 'reservation'

    def get_context_data(self, **kwargs):
        # contex = super(ReservationCreateView, self).get_context_data(**kwargs)
        reservation = Reservation.objects.all()
        form = ReservationCreateForm
        return {'reservation': reservation, 'form': form}

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
            # context['notification'] = 'Эта электронная почта не принадлежит вам'
            # return JsonResponse(self.get_context_data())
        return self.form_invalid(form)

    def form_valid(self, form):
        reservation = form.save()
        if self.email_is_valid(reservation.email):
            return redirect(reverse_lazy('main:main'))
        return redirect(reverse_lazy('main:reservation'))

    def form_invalid(self, form):
        self.get_context_data(notification='Электронная почта не существует')
        return self.render_to_response(self.get_context_data(form=form))

    def email_is_valid(self, email):
        self_email = self.request.user.email
        if self_email == email:
            return True
        return False