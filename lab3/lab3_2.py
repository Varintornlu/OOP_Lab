def add_score(subject_score, student, subject, score):
  if student in subject_score:
      subject_score[student][subject] = score
  else:
      subject_score[student] = {subject: score}
  return subject_score

def calc_average_score(subject_score):
  if not subject_score:
    return "No scores available."

  average_scores = {}

  for student, scores in subject_score.items():
      total_score = sum(scores.values())
      num_subjects = len(scores)
      average_score = total_score / num_subjects
      average_scores[student] = "{:.2f}".format(average_score)

  return average_scores

