from PIL import Image, ImageDraw, ImageFont
import json 
# --------------------------
DOSMyungjo = "./font/DOSMyungjo.ttf"
DOSGothic = "./font/DOSGothic.ttf"
# ===========================================================================================

class StylerManager():
    def get_base_style()->dict:
        mode = 'RGB'
        size = (315, 685)
        color = (255,255,255)
        return {'mode':mode,'size':size,'color':color}
    # --------------------------
    def get_title_style()->dict: #ImageDraw.Draw().text
        font = ImageFont.truetype(DOSMyungjo, 20)
        fill = (0, 0, 0)
        xy = (True,40)
        return {'xy':xy,'font':font, 'fill':fill,'text':'원신 캐릭터 기원 영수증'}
    # --------------------------
    def get_section_line_style()->dict: #ImageDraw.Draw().text
        font = ImageFont.truetype(DOSMyungjo, 20)
        fill = (0, 0, 0)
        xy = (True,0)
        return {'xy':xy,'font':font, 'fill':fill,'text':'--------------------------'}
    # --------------------------
    def get_nomal_text_style()->dict:  #ImageDraw.Draw().text
        font = ImageFont.truetype(DOSGothic, 10)
        fill = (0, 0, 0)
        xy = (True,0)
        align = 'center'
        return {'xy':xy,'font':font, 'fill':fill,'align':align}
    # --------------------------
    def get_bold_text_style()->dict:  #ImageDraw.Draw().text
        style = StylerManager.get_nomal_text_style()
        style.update({'stroke_width' : 0.2,'stroke_fill':style['fill']})
        return style
    # -------------------------------------------------------------------------------------------
    def get_style_by_name(name:str)->dict:
        if name == 'base': return StylerManager.get_base_style()
        elif name == 'title': return StylerManager.get_title_style()
        elif name == 'section_line': return StylerManager.get_section_line_style()
        elif name == 'nomal_text': return StylerManager.get_nomal_text_style()
        elif name == 'bold_text': return StylerManager.get_bold_text_style()
        else: return StylerManager.get_nomal_text_style()

# ===========================================================================================
class ImageEditor():
    def __init__(self):
        self.img = Image.new(**StylerManager.get_base_style())
    # -------------------------------------------------------------------------------------------
    def _get_text_center_xy(self,text,font)->dict:
        w, h = self.img.size
        bbox = ImageDraw.Draw(Image.new('RGB', (200, 100), color='white')).textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        x, y = (w-tw)//2, (h-th)//2
        return {'xy':(x,y)}
    # -------------------------------------------------------------------------------------------
    def draw_text_on_image(self, style_name:str, text:str='', xy:tuple=(False,False))->None:
        style = StylerManager.get_style_by_name(style_name)
        if text or 'text' not in style.keys():
            style.update({'text':text})
        if any([*xy,*map(lambda a:isinstance(a, bool) and a,[*style['xy']])]): #xy입력, 또는 style에 중앙정렬 있음
            # xy/style값이 True이면 중앙정렬, xy가 int이면 해당 값, 나머지는 style 값
            sx,sy = style['xy']
            x,y = xy
            cx,cy = self._get_text_center_xy(style['text'],style['font'])['xy']
            x = cx if any(isinstance(a, bool) and a for a in [x,sx]) else int(x) if not isinstance(x,bool) else sx
            y = cy if any(isinstance(a, bool) and a for a in [y,sy]) else int(y) if not isinstance(y,bool) else sy
            style.update({'xy':(x,y)})
        ImageDraw.Draw(self.img).text(**style)
    # --------------------------
    def increase_image_height(self, n)->None:
        w,h = self.img.size
        style = StylerManager.get_base_style()
        style.update({'size':(w, h+n)})
        img = Image.new(**style)
        img.paste(self.img, (0, 0))
        self.img = img
    # --------------------------
    def get_text_image(self, style_name:str, text:str='')->None:
        style = StylerManager.get_style_by_name(style_name)
        style.update({'xy':(0,0)})
        if text or 'text' not in style.keys():
            style.update({'text':text})
        # --------------------------
        base_style = StylerManager.get_base_style()
        bbox = ImageDraw.Draw(Image.new(**base_style)).textbbox((0, 0), style['text'], font=style['font'])
        base_style.update({'size':(bbox[2] - bbox[0], bbox[3] - bbox[1] + 1)})
        if text.startswith('^'):
            style.update({'text':' '})
        # --------------------------
        img = Image.new(**base_style)
        ImageDraw.Draw(img).text(**style)
        return img
    # -------------------------------------------------------------------------------------------
    def merge_images_vertically(self,images,align = 'center'):
        ws, hs = zip(*(i.size for i in images))
        size = (max(ws),sum(hs))
        base_style = StylerManager.get_base_style()
        base_style.update({'size':size})
        img = Image.new(**base_style)
        # --------------------------
        y = 0
        for i in images:
            x = 0 if align == 'left' else size[0] - i.width if align == 'right' else (size[0] - i.width) // 2
            img.paste(i, (x, y))
            y += i.height
        return img
# ===========================================================================================
class receiptMaker(ImageEditor):
    def __init__(self):
        ImageEditor.__init__(self)
        self.data = self._get_json()
        self.nl = self.get_text_image('nomal_text',text='\n') # new line
        self.sl = self.get_text_image('section_line')         # section_line
    # --------------------------
    def _get_json(self):
        with open('charWishlist.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    
    def _get_body_strings(self):
        body_strings = {'1':{},'2':{},'3':{},'4':{},'5':{},'6':{}}
        for i,w in enumerate(self.data['wishlists']):
            v = w['version_number']
            if '.' not in v : continue
            for p,c in w['wishlist'].items():
                body_strings[v.split('.')[0]].update({f'{v}-{p}':{f"{v} {' | '.join(c)}": ','.join(self.data['results'][i]["wishlist"][p])}})
        return body_strings
    # -------------------------------------------------------------------------------------------
    def _get_header(self):
        imgs = [self.nl,self.sl,self.nl]
        imgs.append(self.get_text_image('title'))
        imgs.append(self.sl)
        imgs.append(self.get_text_image('nomal_text',text='\n여기에 왠지 뭔가를 써놔야 모양이\n잘 나올 것 같다.\n'))
        imgs.append(self.get_text_image('bold_text',text='그래서 아무말이나 씀.\n'))
        imgs.append(self.sl)
        # --------------------------
        return self.merge_images_vertically(imgs)
    # --------------------------
    def add_header(self):
        self.header = self._get_header()
        x = self.img.size[0]//2 - self.header.size[0]//2
        self.img.paste(self.header, (x, 0))
    # -------------------------------------------------------------------------------------------
    def _get_body(self):
        body_strings = self._get_body_strings()
        res= []
        for k,v in body_strings.items():
            limgs,rimgs = [],[]
            for p,wish in v.items():
                r = list(wish.values())[0]
                style_name='nomal_text' if r == '^' else 'bold_text'
                imgs2_text = r + list(wish.values())[0] if r == '^' else list(wish.values())[0]
                limgs. append(self.get_text_image(style_name,text=list(wish.keys())[0]))
                rimgs.append(self.get_text_image('bold_text',text=imgs2_text))
            if not limgs: continue
            left = self.merge_images_vertically(limgs,'left')
            right = self.merge_images_vertically(rimgs,'right')
            # --------------------------
            base_style = StylerManager.get_base_style()
            base_style.update({'size' : (base_style['size'][0], max(left.size[1],right.size[1]))})
            img = Image.new(**base_style)
            img.paste(right, (315-(30+right.size[0]),0))
            img.paste(left, (30,0))
            res.append(self.merge_images_vertically([self.nl,img,self.sl],'center'))
        return self.merge_images_vertically(res,'center')
    # --------------------------
    def add_body(self):
        self.body = self._get_body()
        self.increase_image_height(self.header.size[1] + self.body.size[1] - self.img.size[1])
        self.img.paste(self.body, (0, self.header.size[1]))
    # -------------------------------------------------------------------------------------------
    def _get_footer(self):
        imgs = []
        imgs.append(self.get_text_image('nomal_text',text='\n여기에 왠지 뭔가를 써놔야 모양이\n잘 나올 것 같다.\n'))
        imgs.append(self.get_text_image('bold_text',text='그래서 아무말이나 씀.\n'))
        imgs.append(self.nl)
        # --------------------------
        return self.merge_images_vertically(imgs)
    # --------------------------
    def add_footer(self):
        self.footer = self._get_footer()
        self.img = self.merge_images_vertically([self.img,self.footer])
# ===========================================================================================


if __name__ == '__main__':
    rm = receiptMaker()
    rm.add_header()
    rm.add_body()
    rm.add_footer()
    rm.img.save('./result.jpg')
