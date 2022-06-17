from django.shortcuts import render

# Create your views here.

def calculate_view(request):
    if request.method == "GET":
        return render(request, "calculate.html")
    else:
        answer = 0
        if request.POST.get("calc_method") == "add":
            answer = int(request.POST.get("first_number")) + int(request.POST.get("second_number"))
        elif request.POST.get("calc_method") == "subtract":
            answer = int(request.POST.get("first_number")) - int(request.POST.get("second_number"))
        elif request.POST.get("calc_method") == "multiply":
            answer = int(request.POST.get("first_number")) * int(request.POST.get("second_number"))
        else:
            answer = int(request.POST.get("first_number")) / int(request.POST.get("second_number"))
        context = {
            "first_number": request.POST.get("first_number"),
            "second_number": request.POST.get("second_number"),
            "calc_method": request.POST.get("calc_method"),
            "answer": answer
        }

        return render(request, "answer.html", context)