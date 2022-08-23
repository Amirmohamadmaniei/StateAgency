from django.shortcuts import redirect


class LoginMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(LoginMixin, self).dispatch(request, *args, **kwargs)
