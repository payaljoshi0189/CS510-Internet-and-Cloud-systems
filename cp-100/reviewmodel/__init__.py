# Hannah Galbraith
# Payal Joshi
# CS510 Internet & Cloud Systems Final Project

model_backend = 'datastore'

def get_model():
    """ Configure the model based on what model_backend variable is set to. """
    if model_backend == 'datastore':
        from .model_datastore import model
    else:
        raise ValueError("No appropriate databackend configured. ")
    return model()
