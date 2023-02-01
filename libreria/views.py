from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
from django.contrib.auth import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def links(request):
    return render(request, 'paginas/links.html')

def fotos(request):
    return render(request, 'paginas/fotos.html')

def login(request): 
    return render( request=request, template_name='registration/password_reset_confirm.html', )

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request, id):
    libro= Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')


#def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            # log the user in and then redirect to home page
            authenticated_user = authenticate(username=new_user.username, password=form.cleaned_data['password1'])

            login(request, authenticated_user)

            return HttpResponseRedirect('/')
    else:  # GET method (or any other method) used for rendering the registration page with a blank form object as an argument
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)


#def register_type(self, name: str, instance: Type[T]) -> None:
    self.types[name] = instance

    #@register
    def register_default(self, instance: T) -> None:
        self.defaults.append(instance)

    #@register
    def register_constant(self, name: str, value) -> None:
        self.constants[name] = value

    #@register
    def register_function(self, name: str, func):  # type (str , Callable[[Any], Any])->None : # TODO : check return type of function ?!?!?!!?!??!?!?!!??!?!!!!!???????!!!!!!!???????!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!11111!111111111111111111111!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!11111!111111111111111111111!!!!!!!!!1!!1!!!!""") -> None :# TODO : check return type of function ?!?!?!!?????????????????????????????????????????????!!!??????????"""):  # TODO : check return type of function ?!?!?!!???????!""")) -> None :# TODO : check return type of function ?!?!?!!?""")) -> None ):  # TODO : check return type of function ?!?!?!!?!""")->None:#TODO Check the types ! ! ! !! !! 1 1 1 1 111 11 111 11 111 11 111 11 111 11 111 11 111 11 """)->None:#TODO Check the types ! ! ! !! !! 1 1 1 1 111 11 111 11 111 11 """)->None:#TODO Check the types ! ! ! !! !! 1 """)->None:""", func)

        #@property()
    	def get_functions():
    		    return [f for f in dir(self) if hasattr(_getattribute_(f), "__call__") and not f.startswith("__")]


# Create user and save to the database
#user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# Update fields and then save again
#user.first_name = 'John'
#user.last_name = 'Citizen'
#user.save()