from django.shortcuts import render


class UIDisplay:

    @staticmethod
    def alert(request, view, type, message):
        return render(request, view, {"alert": {
            "message": message,
            "type": type
        }})
