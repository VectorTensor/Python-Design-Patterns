from reactivex import Observable, create


def get_quotes():
    import contextlib, io

    zen = io.StringIO()

    with contextlib.redirect_stdout(zen):
        import this

    quotes = zen.getvalue().split('\n')[1:]
    return quotes


def push_quotes(obs, sch):
    quotes = get_quotes()
    for q in quotes:
        if q:
            obs.on_next(q)
        else:
            obs.on_next('No quotes')

    obs.on_completed()


source = create(push_quotes)
source.subscribe(on_next=lambda x: print(x), on_completed=lambda: print('completed'), on_error=lambda e: print(e))
