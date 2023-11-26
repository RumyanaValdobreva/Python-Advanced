# Python Advanced Exam - 17 June 2023

def gather_credits(credits, *args):
    credits_earned = 0
    enrolled_courses = []

    for course_name, course_credits in args:
        if credits_earned >= credits:
            break
        if course_name in enrolled_courses:
            continue
        enrolled_courses.append(course_name)
        credits_earned += course_credits

    if credits_earned >= credits:
        return f"""Enrollment finished! Maximum credits: {credits_earned}.
Courses: {', '.join(sorted(enrolled_courses))}"""

    else:
        credits_shortage = credits - credits_earned
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."
