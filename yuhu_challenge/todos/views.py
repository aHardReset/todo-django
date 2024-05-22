from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView, UpdateView

from .forms import ToDoDelete, ToDoForm
from .models import ToDoItem


class CombinedTodoView(LoginRequiredMixin, TemplateView):
    model = ToDoItem
    form_create = ToDoForm
    form_delete = ToDoDelete
    template_name = "todos/todo_list.html"

    def _get_context(self, request, reset_form: bool = True):
        context = {}
        context["form"] = self.form_create()
        paginator = Paginator(
            self.model.objects.filter(user__email=request.user.email).order_by(
                "-created_at"
            ),
            5,
        )
        page_number = 1
        form = self.form_create()

        if request.method == "GET":
            page_number = request.GET.get("page", 1)

        if request.method == "POST" and not reset_form:
            form = self.form_create(request.POST)

        todos = paginator.get_page(page_number)
        context["todos"] = todos
        context["form"] = form
        return context

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self._get_context(request))

    def post(self, request, *args, **kwargs):
        form = self.form_create(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        return self.render_to_response(self._get_context(request, form.is_valid()))


class ToDoDeleteView(LoginRequiredMixin, DeleteView):
    model = ToDoItem
    success_url = reverse_lazy("todos:list")


class ToDoUpdateView(LoginRequiredMixin, UpdateView):
    model = ToDoItem
    form_class = ToDoForm
    template_name = "todos/update_todo.html"
    success_url = reverse_lazy("todos:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


import json


class ToogleToDoView(View):
    model = ToDoItem

    def patch(self, request, *args, **kwargs):
        data = json.loads(request.body)
        pk = data.get("pk")
        record = self.model.objects.get(pk=pk)
        record.is_done = not record.is_done
        record.save()
        return HttpResponse(status=204)
