from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.conf import settings
from django.core.mail import send_mail


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
        if not (self.request.user.is_authenticated):
            return redirect(reverse_lazy('auth:login'))
        return render(self.request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
            # context['notification'] = 'Эта электронная почта не принадлежит вам'
            # return JsonResponse(self.get_context_data())
        return self.form_invalid(form)

    def form_valid(self, form):
        reservation = form.save(commit=False)
        reservation.email = self.request.user.email
        reservation.save()
        return redirect(reverse_lazy('main:main'))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class GetAnswer(DetailView):
    model = Reservation
    template_name = 'photosession/mailAnswer.html'
    context_object_name = 'reservation'

    def get_context_data(self, **kwargs):
        model = get_object_or_404(Reservation, pk=self.kwargs['pk'])
        context = {
            'email': model.email
        }
        return context

    def get(self, request, *args, **kwargs):
        return JsonResponse(self.get_context_data())

    def post(self, request, *args, **kwargs):
        user = CustomUser.objects.filter(email=self.get_context_data().get('email'))
        reservation = self.model
        if self.request.POST.get('status') == 'accept':
            reservation.status = '2'
        else:
            reservation.status = '0'
        headers = {'Для': '{} <{}>'.format(user.model.username, user.model.email)}
        send_mail('Ответ на заявку', self.request.POST.get('answer'), settings.EMAIL_HOST_USER, [self.get_context_data().get('email')], headers)
        return JsonResponse(self.get_context_data())