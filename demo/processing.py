import db_connection

def init_hesomon():
    subjects = ["Toan", "Ngu Van", "Sinh hoc", "Vat Ly", "Hoa hoc", "Lich su", "Dia ly", "Ngoai ngu", "The duc", "Cong nghe", "Tin hoc", "Nghe thuat"]
    skills = ["SUY LUẬN", "XỬ LÝ", "GHI NHỚ", "KĨ THUẬT", "SỨC KHOẺ", "SÁNG TẠO", "CẢM XÚC", "GIAO TIẾP"]
    data = [[4.5,	4.6,	2.3,	1.2,	0.6,	3.2,	1.4,	1.3],
            [3.2,	2.3,	3.5,	0.4,	0.7,	4.3,	4.6,	4.2],
            [3.7,	3.4,	3.7,	3.2,	0.3,	2.3,	2.3,	3.4],
            [4.3,	4.5,	3.2,	3.4,	0.5,	2.5,	1.5,	1.2],
            [4.4,	3.7,	3.5,	3.7,	0.8,	3.3,	1.8,	1.4],
            [2.3,	2.4,	4.3,	2.0,	0.9,	2.3,	2.3,	1.5],
            [2.7,	2.2,	4.2,	2.3,	0.7,	2.6,	1.2,	2.2],
            [3.4,	3.1,	3.6,	1.7,	0.8,	2.5,	3.2,	4.3],
            [0.4,	0.5,	1.2,	0.6,	4.8,	1.2,	1.4,	2.4],
            [3.4,	2.8,	2.5,	4.8,	0.8,	3.7,	1.8,	2.4],
            [4.5,	4.8,	2.8,	4.3,	0.8,	3.2,	1.5,	2.8],
            [2.3,	2.1,	1.8,	2.6,	0.4,	4.7,	4.6,	4.2]]

    subject_skill = {}

    for i in subjects:
        subject_skill[i] = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            subject_skill[subjects[i]][skills[j]] = data[i][j]

    return subject_skill

def processing_subject(data):
    subjects = ["Toan", "Ngu Van", "Sinh hoc", "Vat Ly", "Hoa hoc", "Lich su", "Dia ly", "Ngoai ngu", "The duc", "Cong nghe", "Tin hoc", "Nghe thuat"]
    score = {}

    for i in subjects:
        score[i] = 0

    for subject in subjects:
        sum_heso = 0
        for d in data:
            if d['subject_name'] == subject:
                score[subject] += d['exam_heso']*d['exam_score']
                sum_heso += d['exam_heso']
        if (sum_heso != 0):
            score[subject] /= sum_heso
        else:
            score[subject] = 0
        
    return score

def processing_skill(data):
    hesomon = init_hesomon()
    skills = ["SUY LUẬN", "XỬ LÝ", "GHI NHỚ", "KĨ THUẬT", "SỨC KHOẺ", "SÁNG TẠO", "CẢM XÚC", "GIAO TIẾP"]
    score = {}
    sum_heso = {}

    for skill in skills:
        score[skill] = 0
        sum_heso[skill] = 0
    for d in data:
        for skill in hesomon[d]:
            score[skill] += hesomon[d][skill]*data[d]
            sum_heso[skill] += hesomon[d][skill]
    
    for i in score:
        score[i] /= sum_heso[i]
    print(score)
    return score

def processing_skill_value(data):
    rr = processing_skill(data)
    res = []
    for i in rr:
        res.append(rr[i])
    print(res)
    return res;

def get_score(student_id):
    db = db_connection.db_connection()
    data = db.query("SELECT student.student_id, student.student_name, Exam.subject_id, subject.subject_name, Exam.exam_id, exam_name, exam_heso, exam_score, exam_date FROM Student, student_subject, subject, Exam WHERE student.student_id = student_subject.student_id and student_subject.subject_id = Subject.subject_id and subject.subject_id = Exam.subject_id and student.student_id = '" + student_id + "'")
    header = ["student_id", "student_name", "subject_id", "subject_name", "exam_id", "exam_name", "exam_heso", "exam_score", "exam_date"]
    rr = []
    for i in data:
        rt = {}
        for j in range(len(header)):
            rt[header[j]] = i[j]
        rr.append(rt)
    return rr;
    

