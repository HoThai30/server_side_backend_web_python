
APP_VALUE_STATUS_ACTIVE = 'published'
APP_VALUE_LAYOUT_DEFAULT = 'list'
APP_VALUE_STATUS_DEFAULT = 'draft'
APP_VALUE_STATUS_ORDER_DEFAULT = 'order'
APP_PATH_PAGES = 'shop/pages/'
APP_VALUE_IMAGES_DEFAULT = '/media/news/images/feed/no_img.jfif'

TABLE_PLANTING_METHOD_SHOW = 'Planting method'
TABLE_CATEGORY_SHOW = "Category"
TABLE_PRODUCT_SHOW =  "Product"  
TABLE_CONTACT_SHOW = "Contact"
TABLE_ORDER_SHOW = "Order"

APP_VALUE_STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')  # Sửa "Publisher" thành "Published"
    )


APP_VALUE_LAYOUT_CHOICE = (
        ('list', 'List'),
        ('grid', 'Grid')
    )
APP_VALUE_STATUS_ORDER_CHOICES  = (
    ('order', 'Order'),
    ('confirm', 'Confirm'),
    ('delivery', 'Delivery'),
    ('finish', 'Finish'),
)
    
SETTING_ARTICLE_TOTAL_ITEMS_SPECIAL = 5
SETTING_ARTICLE_TOTAL_ITEMS_PER_PAGE = 8
SETTING_ARTICLE_TOTAL_ITEMS_RELATED = 6
SETTING_PRICE_COIN_TOTAL_ITEMS  = 5
SETTING_PRICE_GOLD_TOTAL_ITEMS  = 5
SETTING_ARTICLE_TOTAL_ITEMS_RAMDOM = 3
SETTING_ARTICLE_TOTAL_ITEMS_RECENT = 5
SETTING_FEED_TOTAL_ITEMS_SIDEBAR = 5
SETTING_CATEGORY_TOTAL_ITEMS_SIDEBAR = 5
SETTING_CATEGORY_TOTAL_ITEMS_MENU = 6

SETTING_PRODUCT_TOTAL_ITEMS_RELATED = 6
SETTING_PRODUCT_TOTAL_ITEMS_SPECIAL_INDEX = 8
SETTING_PRODUCT_TOTAL_ITEMS_LATEST_INDEX = 9
SETTING_PRODUCT_TOTAL_ITEMS_LATEST_SIDEBAR = 9
SETTING_PRODUCT_TOTAL_ITEMS_HOT_INDEX = 9
SETTING_PRODUCT_TOTAL_ITEMS_RAMDOM_INDEX = 9
SETTING_CATEGORY_TOTAL_ITEMS_SIDEBAR  = 6
SETTING_PLANTING_METHOD_TOTAL_ITEMS_SIDEBAR = 4
SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE = 3
SETTING_PRODUCT_TOTAL_ITEMS_PER_PAGE = 2

SETTING_API_LINK_PRICE_COIN = "http://apiforlearning.zendvn.com/api/get-coin"
SETTING_API_LINK_PRICE_GOLD = "http://apiforlearning.zendvn.com/api/get-gold"


ADMIN_SRC_JS = ('my_admin/js/general.js', 'my_admin/js/jquery-3.6.0.min.js', 'my_admin/js/slugify.min.js')

# ADMIN_SRC_CSS  = {'all:'('my_admin/css/custom.css',)}
ADMIN_HEADER_NAME = 'news admin'

NOTIFY_ORDER_SUCCESS = 'Đặt hàng thành công!'
NOTIFY_CONTAC_SUCCESS = 'Cảm ơn bạn đã liên hệ với chúng tôi. Chúng tôi sẽ phản hồi lại bạn sớm nhất có thể.'
NOTIFY_ORDER_CHECK_NOT_EXIST = "Bạn chưa nhập mã đơn hàng"
NOTIFY_ORDER_CHECK_NOT_NULL = "Không tìm thấy mã đơn hàng"