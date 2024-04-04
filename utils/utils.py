"""treatment of the search ouputs results"""
from utils.fhir_api import search_code


def get_implicit_valueset(codesystem: dict) -> list | None:
    """
    Return the implicit ValueSets availables for CodeSystem
    Args:
        codesystem (dict): Dictionary containing the information from each CodeSystem
        available in the SMT server.
    Returns:
        list|None: List of implicit valuesets
    """

    imp_vs = []
    for vs in codesystem["entry"]:
        if "valueSet" in vs["resource"]:
            imp_vs.append(vs["resource"]["valueSet"])
    return imp_vs


def get_code_label(result: dict) -> dict | None:
    """
    Obtaining the label and vocabulary for a searched code

    Args:
        result (dict): result from search_code function

    Returns:
        dict | None: a dictionary containing the code, the label and the vocabulary
        for the searched code.
    """

    code = None
    label = None
    vocabulary = None

    for i in result["parameter"]:
        if i["name"] == "code":
            code = i["valueCode"]

        if i["name"] == "display":
            label = i["valueString"]

        if i["name"] == "name":
            vocabulary = i["valueString"]

    return {"code": code, "label": label, "vocabulary": vocabulary}


def get_relations(token: str, result: dict) -> dict | None:
    """
    Get the ontological relationships or the hierarchies of a searched code.

    Args:
        result (dict): result from search_code function

    Returns:
        dict | None: a dictionary containing the relationships (parent and children)
        of a given code.
    """
    parents = []
    children = []
    relations = {"parents": [], "children": []}

    for parameter in result["parameter"]:

        if parameter["name"] == "system":
            url = parameter["valueUri"]

        if parameter["name"] == "property":

            if parameter["part"][0]["valueCode"] == "parent":
                parent = parameter["part"][1]["valueCode"]
                parents.append(parent)

            if parameter["part"][0]["valueCode"] == "child":
                child = parameter["part"][1]["valueCode"]
                children.append(child)

    for parent in parents:
        codes_parents = search_code(token=token, url=url, code=parent)  # type: ignore
        relations["parents"].append(get_code_label(codes_parents))  # type: ignore

    for child in children:
        codes_children = search_code(token=token, url=url, code=child)  # type: ignore
        relations["children"].append(get_code_label(codes_children))  # type: ignore

    return relations
