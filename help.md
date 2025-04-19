 - tạo project mới: django-admin startproject mysite
 - tạo app mới: python manage.py startapp polls
 
 
 # nhúng và tối ưu hóa giao diện -->
 - xây dựng thành phần chung
 - tạo layout và dùng block content(hạn chế lặp các phần tử html)
 - xây dựng các layout con (multi layout)
 # xây dựng trang hiển thị category
 
 - dùng get_object_or_404 để tìm dữ liệu trong csdl
 - lọc bài viết thêm category, status và published_date
 - sắp xếp bài viết mới nhất lên trước
 - phân trang dùng paginator
 - render html và truyền ra biến dữ liệu để sử dụng template
 - sử dụng cú pháp đổ dữ liệu và các câu lệnh if else for trong django
 - hàm format ngày tháng và rút gọn nội dung

 # xây dựng trang hiển thị nội dung bài viết
 -  định nghĩa hàm get_absolute_url tối ưu việc thay thế đường dẫn
 - xóa bài viết dư thừa ở phần bài viết liên quan

 # xây dựng trang chủ
 - dùng slice để giới hạn bài viết hiển thị
 # xây dựng chức năng tìm kiếm
 - một số lookup để tìm kiến
 - contains: tìm kiếm các giá trị có chứa một chuỗi con cụ thể
 - icontains:  //                    //                  //   (ko phân biệt chữ hoa thường)
 - regex: tìm kiếm các giá trị phù hợp với một biểu thức chính quy cụ thể
 - iregex:                          //                                     (ko phân biệt chữ hoa thường)
 
 
 
 python manage.py runserver

 python manage.py migrate
 
 python manage.py makemigrations 