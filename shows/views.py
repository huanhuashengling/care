from django.shortcuts import render
from picks.models import Student, Sclass, EvaluateLog, EvaluateItem, EvaluateIndex

# import sys
# Create your views here.
# sys.path.append('../')
def index(request):
    content = {"dataset": "I am a index page"}
    return render(request, 'shows/index.html', content)

def wait(request):
    content = {"dataset": "I am a wait page"}
    return render(request, 'shows/wait.html', content)

def show(request):
    identity_number = request.GET["identity_number"]
    student = Student.objects.filter(identity_number=identity_number).first()
    sclass = Sclass.objects.filter(id=student.sclasses_id).first()

    evaluate_logs = EvaluateLog.objects.filter(students_id=student.id)
    evaluate_log_count = evaluate_logs.count()

    result_score = 0
    right_count = 0
    wrong_count = 0
    evaluate_teachers = []
    for evaluate_log in evaluate_logs:
        evaluate_items = EvaluateItem.objects.filter(id=evaluate_log.evaluate_items_id, sclasses_id=sclass.id)
        if (evaluate_log.teachers_id not in evaluate_teachers):
            evaluate_teachers.append(evaluate_log.teachers_id)
        for evalute_item in evaluate_items:
            result_score += evalute_item.score
            if evalute_item.score > 0:
                right_count += 1
            else:
                wrong_count += 1
    
    evaluate_teacher_count = len(evaluate_teachers)

    # print(student.student_name)
    class_title = sclass.grade_name + "年级" + sclass.class_name + "班"
    dataset = {"student_name": student.student_name, 
                "class_title": class_title, 
                "evaluate_log_count": evaluate_log_count, 
                "result_score": result_score,
                "right_count": right_count,
                "wrong_count": wrong_count,
                "evaluate_teacher_count": evaluate_teacher_count,
                }
    # dataset = {"dataset": "I am a show page" + request.GET["identity_number"]}
    return render(request, 'shows/show.html', dataset)
