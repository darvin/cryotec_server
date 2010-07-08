from machines.models import MachineType, Machine
def machines_tree(request):
    mtypes = MachineType.objects.all()
    return  {"machine_types":mtypes}