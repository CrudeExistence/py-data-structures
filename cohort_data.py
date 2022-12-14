"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()


    cohort_data = open('cohort_data.txt')

    
    for line in cohort_data:
      data = line.rstrip().split('|')[2]
      if data:
        houses.add(data)


    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []


    file_name = open(filename)

    for line in file_name:

      first, last, _, _, cohort_name = line.rstrip().split('|')
      # cohort.lower()
      # if cohort == 'all':
      #   students.append(f'{first} {last}')
      # elif cohort in cohort_name:
      #   if cohort == cohort_name:
      #     students.append(f'{first} {last}')
      # else:
      #   students.append(f'{first} {last}')

      if cohort_name not in ('I', 'G') and cohort in ('All', cohort_name):
        students.append(f'{first} {last}')



    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []


    rosters = open(filename)

    for line in rosters:
      first, last, house, _, cohort = line.rstrip().split('|')
      if house == "Dumbledore's Army":
        dumbledores_army.append(f"{first} {last}")
      elif house == "Gryffindor":
        gryffindor.append(f"{first} {last}")
      elif house == "Hufflepuff":
        hufflepuff.append(f"{first} {last}")
      elif house == "Ravenclaw":
        ravenclaw.append(f"{first} {last}")
      elif house == "Slytherin":
        slytherin.append(f"{first} {last}")
      elif house == "":
        if cohort == "G":
          ghosts.append(f"{first} {last}")
        elif cohort == "I":
          instructors.append(f"{first} {last}")
        

    return [sorted(dumbledores_army),
            sorted(gryffindor),
            sorted(hufflepuff),
            sorted(ravenclaw),
            sorted(slytherin),
            sorted(ghosts),
            sorted(instructors)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    data_file = open(filename)
    
    for line in data_file:
      first, last, house, teacher, cohort = line.rstrip().split('|')
      all_data.append((f"{first} {last}", house, teacher, cohort))


    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Someone else')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    data_file = open(filename)
    
    for line in data_file:
      first, last, _, _, cohort = line.rstrip().split('|')

      full_name = f'{first} {last}'

      if name == full_name:
        return cohort

    return None


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    data_file = open(filename)
    last_names = set()
    dupes = set()

    for line in data_file:
      _, last, _, _, _ = line.rstrip().split('|')
      if last in last_names:
        dupes.add(last)
      else:
        last_names.add(last)
      
    
    return dupes


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # file_data = open(filename)

    housemates = set()
    student = None

    for person in all_data(filename):
      full_name, house, teacher, cohort = person
      
      if full_name == name:
        student = person
        break

    if student:
      student_name, student_house, _, student_cohort = student

      for full_name, house, _, cohort in all_data(filename):
        if ((house, cohort) == (student_house, student_cohort) and full_name != name):
          housemates.add(full_name)

    return housemates



##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
