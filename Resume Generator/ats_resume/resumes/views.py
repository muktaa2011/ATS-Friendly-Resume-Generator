

# Create your views here.
from django.shortcuts import render

from ai_engine.ai_services import get_ai_suggestions
from .models import Resume
from .utils.pdf_generator import generate_resume_pdf
from .forms import ResumeForm
from ats.scoring import calculate_ats_score


def resume_form(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()

            ats_score, suggestions = calculate_ats_score(resume.skills)
            return render(request, 'ats_result.html', {
                'score': ats_score,
                'suggestions': suggestions
            })
    else:
        form = ResumeForm()

    return render(request, 'resume_form.html', {'form': form})


def generate_resume_view(request):
    resume = Resume.objects.latest('id')
    pdf_path = generate_resume_pdf(resume)
    return pdf_path


def get_suggestions_view(request):
    if request.method == 'POST':
        resume = Resume.objects.latest('id')
        resume_text = resume.skills + " " + resume.experience + " " + resume.education
        job_description = request.POST.get("job_description", "")

        suggestions = get_ai_suggestions(resume_text, job_description)
        job_desc = request.POST.get("job_description")
        ats_score = calculate_ats_score(
            resume.skills + resume.experience,
            job_desc
        )

        return render(request, 'suggestions.html', {
            'suggestions': suggestions,
            'ats_score': ats_score
        })
