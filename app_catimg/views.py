from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# View para exibir os cards de imagens
def image_cards(request):
    return render(request, 'image_cards.html')

# View para processar a imagem selecionada e retornar a resposta via htmx
def show_image(request):
    img = request.GET.get('img', '')
    if img:
        html_content = render_to_string('selected_image.html', {'img': img})
        return HttpResponse(html_content)
    return HttpResponse('<p>Erro: Imagem não encontrada.</p>')
