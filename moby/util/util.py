from django.core.paginator import Paginator

class Util:
    
    @staticmethod
    def pagination(object, pages, request):
        pagi_obj = Paginator(object, pages)
        page_num = request.GET.get('page')
        page = pagi_obj.get_page(page_num)

        return page