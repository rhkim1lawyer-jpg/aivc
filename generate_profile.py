"""김래현 변호사 소개 자료 PDF 생성"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# 한글 지원 폰트 등록
pdfmetrics.registerFont(TTFont("WQY", "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc", subfontIndex=0))

OUTPUT = "김래현_변호사_소개자료.pdf"
W, H = A4

# 색상
NAVY = HexColor("#1a1a2e")
ACCENT = HexColor("#c0392b")
DARK = HexColor("#2c3e50")
GRAY = HexColor("#7f8c8d")
LIGHT_BG = HexColor("#f5f6fa")
WHITE = HexColor("#ffffff")


def draw_header(c):
    """상단 헤더 영역"""
    # 네이비 배경
    c.setFillColor(NAVY)
    c.rect(0, H - 90 * mm, W, 90 * mm, fill=True, stroke=False)

    # 이름
    c.setFillColor(WHITE)
    c.setFont("WQY", 32)
    c.drawString(25 * mm, H - 35 * mm, "김래현")

    c.setFont("WQY", 14)
    c.drawString(25 * mm, H - 48 * mm, "변호사 | Attorney at Law")

    # 악센트 라인
    c.setStrokeColor(ACCENT)
    c.setLineWidth(3)
    c.line(25 * mm, H - 55 * mm, 85 * mm, H - 55 * mm)

    # 연락처 정보
    c.setFont("WQY", 9)
    c.setFillColor(HexColor("#bdc3c7"))
    contact_y = H - 68 * mm
    c.drawString(25 * mm, contact_y, "Email: rhkim@lawfirm.co.kr")
    c.drawString(25 * mm, contact_y - 5 * mm, "Tel: 02-XXX-XXXX")
    c.drawString(25 * mm, contact_y - 10 * mm, "Mobile: 010-XXXX-XXXX")


def draw_section_title(c, y, title):
    """섹션 제목"""
    c.setFillColor(ACCENT)
    c.rect(25 * mm, y - 1 * mm, 3 * mm, 7 * mm, fill=True, stroke=False)
    c.setFillColor(DARK)
    c.setFont("WQY", 14)
    c.drawString(32 * mm, y, title)
    return y - 12 * mm


def draw_text(c, y, text, indent=32 * mm, size=10, color=DARK):
    """본문 텍스트"""
    c.setFont("WQY", size)
    c.setFillColor(color)
    c.drawString(indent, y, text)
    return y - 6 * mm


def draw_bullet(c, y, text, indent=35 * mm):
    """불릿 포인트"""
    c.setFont("WQY", 10)
    c.setFillColor(DARK)
    c.drawString(indent - 4 * mm, y, "·")
    c.drawString(indent, y, text)
    return y - 7 * mm


def generate():
    c = canvas.Canvas(OUTPUT, pagesize=A4)

    draw_header(c)

    y = H - 100 * mm

    # === 인사말 ===
    y = draw_section_title(c, y, "인사말")
    greetings = [
        "안녕하세요. 김래현 변호사입니다.",
        "의뢰인의 권리 보호를 최우선으로,",
        "신뢰와 전문성을 바탕으로 최선의 법률 서비스를 제공합니다.",
    ]
    for line in greetings:
        y = draw_text(c, y, line)
    y -= 5 * mm

    # === 학력 ===
    y = draw_section_title(c, y, "학력")
    education = [
        "OO대학교 법학전문대학원 졸업 (법학전문석사)",
        "OO대학교 졸업 (학사)",
    ]
    for item in education:
        y = draw_bullet(c, y, item)
    y -= 5 * mm

    # === 경력 ===
    y = draw_section_title(c, y, "주요 경력")
    career = [
        "변호사 시험 합격 (제O회)",
        "대한변호사협회 등록",
        "법률사무소 OOO 소속 변호사",
        "OO지방법원 국선변호인",
    ]
    for item in career:
        y = draw_bullet(c, y, item)
    y -= 5 * mm

    # === 주요 업무 분야 ===
    y = draw_section_title(c, y, "주요 업무 분야")
    areas = [
        "민사소송 (손해배상, 계약분쟁, 부동산)",
        "형사사건 (변호 및 고소·고발 대리)",
        "가사사건 (이혼, 상속, 양육권)",
        "기업법무 (계약서 검토, 자문)",
        "행정소송 및 헌법소원",
    ]
    for item in areas:
        y = draw_bullet(c, y, item)
    y -= 5 * mm

    # === 주요 성과 ===
    y = draw_section_title(c, y, "주요 성과 및 활동")
    achievements = [
        "OOO 사건 대법원 승소 판결 이끌어냄",
        "기업 법률 자문 다수 수행",
        "법률 칼럼 및 강의 활동",
        "무료 법률 상담 봉사 활동",
    ]
    for item in achievements:
        y = draw_bullet(c, y, item)

    # === 하단 ===
    c.setFillColor(NAVY)
    c.rect(0, 0, W, 20 * mm, fill=True, stroke=False)
    c.setFillColor(HexColor("#bdc3c7"))
    c.setFont("WQY", 8)
    c.drawCentredString(W / 2, 8 * mm, "본 자료는 김래현 변호사 소개 목적으로 작성되었습니다.  |  내용 수정이 필요하시면 말씀해 주세요.")

    c.save()
    print(f"PDF 생성 완료: {OUTPUT}")


if __name__ == "__main__":
    generate()
