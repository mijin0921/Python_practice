#import, from, as키워드

# import를 이용해서 모듈을 임포트 한다.

# as 키워드를 이용해서 모듈 이름을 단축 시킬 수 있다.
import lottomuchine as lt

# from~import 키워드를 사용해서 모듈의 특정 기능만 사용할 수 있다.
# from calculator import add
from calculator import add,sub
add(1,2)
sub(1,2)