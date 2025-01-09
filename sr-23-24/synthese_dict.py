from functools import reduce


def synthese_dict(employees):
    servicesWithValues = list(
        map(lambda emp: {"service": employees[emp]['service'], "salaire": employees[emp]['salaire']}, employees)
    )

    synthese_data = reduce(lambda data, service: {
        **data,
        service["service"]: [
            min(data[service["service"]][0], service["salaire"]) if service["service"] in data else service["salaire"],
            data[service["service"]][1] + service["salaire"] if service["service"] in data else service["salaire"],
            (data[service["service"]][1] + service["salaire"]) / (data[service["service"]][2] + 1) if service[
                                                                                                          "service"] in data else
            service["salaire"]
        ] if service["service"] in data else [service["salaire"], service["salaire"], 1]
    }, servicesWithValues, {})

    return synthese_data
