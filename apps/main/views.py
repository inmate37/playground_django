# Django
from django.http.request import HttpRequest
from django.shortcuts import (
    HttpResponse,
    render
)

# First party
from abstracts.decorators import performance_counter


def simple(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        '<h1>Что нибудь</h1>'
    )


@performance_counter
def test_performance(request: HttpRequest) -> HttpRequest:
    """test_performance."""

    numbers: list[int] = [_ for _ in range(50_000_000)]  # pylint: disable=R1721

    ctx_data: dict[str, str | list[int]] = {
        'ctx_title': 'Заголовок главной страницы',
        'ctx_numbers': numbers[:10]
    }
    return render(
        request,
        template_name='main/index.html',
        context=ctx_data
    )


@performance_counter
def index(request: HttpRequest) -> HttpRequest:
    """index view."""

    numbers: list[int] = []
    i: int
    for i in range(1, 11):
        numbers.append(i)

    ctx_data: dict[str, str | list[int]] = {
        'ctx_title': 'Заголовок главной страницы',
        'ctx_numbers': numbers
    }
    return render(
        request,
        template_name='main/index.html',
        context=ctx_data
    )
