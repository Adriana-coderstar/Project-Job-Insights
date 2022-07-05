from src.jobs import read


def get_unique_job_types(path):

    jobs = read(path)

    unique_jobs_types = set()

    for job_list in jobs:
        if job_list["job_type"] != "":
            unique_jobs_types.add(job_list["job_type"])

    return list(unique_jobs_types)


def filter_by_job_type(jobs, job_type):

    job_type_dic = []

    for job in jobs:
        if job["job_type"] == job_type:
            job_type_dic.append(job)
    return job_type_dic


def get_unique_industries(path):

    industry = read(path)

    industry_list = set()

    for ind_data in industry:
        if ind_data["industry"] != "":
            industry_list.add(ind_data["industry"])

    return list(industry_list)


def filter_by_industry(jobs, industry):
    job_dic_industry = []

    for job in jobs:
        if job["industry"] == industry:
            job_dic_industry.append(job)
    return job_dic_industry


def get_max_salary(path):

    jobs = read(path)

    higher_salary = set()

    for job_salary in jobs:
        if job_salary["max_salary"].isnumeric():
            higher_salary.add(int(job_salary["max_salary"]))

    return max(higher_salary)


def get_min_salary(path):
    jobs = read(path)

    min_salary = set()

    for job_salary in jobs:
        if job_salary["min_salary"].isnumeric():
            min_salary.add(int(job_salary["min_salary"]))

    return min(min_salary)


def matches_salary_range(job, salary):

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError

    elif (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError

    elif job["min_salary"] > job["max_salary"]:
        raise ValueError

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
