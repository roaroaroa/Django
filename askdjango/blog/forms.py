from django import forms
from .models import Comment
from .models import Board
#장고 form ,modelform이 있는데 form을 사용하게 되면 안에 들어가는 필드를 모두 정의해줘야 하는데, 
#modelform을 쓰게 되면 지정된 모델로부터 각 필드 정보를  읽어서  form필드를  자동생성해 줄 수 있습니다. 


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요')

class PostForm(forms.Form):
    title=forms.CharField(validators=[min_length_3_validator])
    content=forms.CharField(widget=forms.Textarea())

class CheckForm(forms.Form):
    rice=forms.BooleanField(required=False)
    water=forms.BooleanField(required=False)
    tissue=forms.BooleanField(required=False)

class  CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        #fields  =_all_  #모델에 있는 필드를 모두 사용
        fields =('name', 'content')  # 모델에 있는 name과 content 필드만 이용하겠다. 

class  BoardForm(forms.ModelForm):
    class Meta:
        model=Board
        #fields  ='__all__'  #모델에 있는 필드를 모두 사용 _ 두개-->__
        fields =('subject', 'name','memo')  # 모델에 있는 name과 content 필드만 이용하겠다. 


        

