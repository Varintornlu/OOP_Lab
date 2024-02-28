def add_score(subject_score, subject, score):
  subject_score[subject] = score
  return subject_score


def calc_average_score(subject_score):
  if not subject_score:
    return "No scores available."

  total_score = sum(subject_score.values())
  num_subjects = len(subject_score)
  average_score = total_score / num_subjects

  return "{:.2f}".format(average_score)