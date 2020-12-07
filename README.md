# scrappy_crawl
BÁO CÁO
VIDEO CRAWLING TOOL

1.	Tổng quan
Một cách tổng quát, các website chuyên đăng tải video đều sử dụng javascript thực thi một đoạn lệnh nào đó để tải và hiển thị video lên trình duyệt của người sử dụng, và có rất ít website thực hiện việc nhúng trực tiếp video vào đoạn mã HTML của trang web. Thông thường, các thư viện dùng để đọc mã nguồn của website như Beautiful Soup hay Request chỉ có khả năng tải được mã HTML. Với các trang web sử dụng javascript để hiển thị toàn bộ nội dung website thì các thư viện trên không thể hoạt động hiệu quả, do khi vừa truy xuất vào website, các thành phần trong website sẽ không được tải lên đầy đủ qua mã HTML mà được tải nhờ đoạn mã javascript – đa số các video cũng được tải tương tự theo cách thức này.
Do đó, để có thể thu thập video một cách tự động thông qua các đoạn lệnh, công cụ phải có khả năng đọc được website một cách đầy đủ kể cả khi trang này được tải thông qua javascript. Để thu thập được các video này, ta cần phải tìm được tới nguồn nơi chứa video, thường là thông qua thuộc tính src trong tag video. Một vấn đề khác xuất phát từ việc tìm nguồn của video đó là thông thường các website chuyên cung cấp dịch vụ xem phim sẽ sử dụng các nền tảng player để có thể cung cấp trải nghiệm xem phim tốt cho người dùng. Các nền tảng player này rất đa dạng và đều có cách thức hoạt động riêng do đó việc có thể viết một công cụ có thể hoạt động được trên tất cả trang web gần như là bất khả thi.
Trong báo cáo này, công cụ thu thập video tự động được viết riêng và có khả năng hoạt động tốt trên trang web xnxx.com. Công cụ sử dụng ngôn ngữ Python với 2 thành phần chính sau:
-	Splash: một trình duyệt đơn giản giúp tải những website được viết bằng javascript
-	Scrapy: thư viện hỗ trợ thu thập dữ liệu
Bên cạnh Splash còn có một số công cụ khác dùng để load javascript ví dụ như thư viện Request của Python hoặc Selenium. Thư viện Requests vốn là một thư viện quen thuộc trong việc đọc dữ liệu từ website, đặc biệt module Requests-HTML được xem là bản nâng cấp của Requests có khả năng hiển thị javascript tuy nhiên chỉ hạn chế tại phiên bản Python 3.6 và có tương đối ít tài liệu tham khảo. Nếu Requests là thư viện hỗ trợ việc đọc các dữ liệu từ website thì Selenium là công cụ giả lập một trình duyệt để thực hiện các thao tác như người dùng đang duyệt web thực thụ. Selenium cho phép chạy nhiều loại trình duyệt khác nhau như Google Chrome, Firefox,… Selenium là một công cụ rất mạnh mẽ trong việc mô phỏng các thao tác trên website, tuy nhiên là quá cồng kềnh cho một công cụ thu thập dữ liệu với mục đích tích hợp vào add-on. Bên cạnh đó, mỗi lần khởi chạy Selenium cũng sẽ tạo ra một tiến trình trình duyệt gây tiêu tốn nhiều tài nguyên của hệ thống.
2.	Cài đặt công cụ
2.1.	Cài đặt Docker và Splash
Splash chạy trên Docker, do đó trước tiên người sử dụng cần cài đặt Docker và pull image qua câu lệnh sau:
$ sudo docker pull scrapinghub/splash
Sử dụng Docker để mở Splash trên port 8050:
$ sudo docker run -p 8050:8050 scrapinghub/splash
2.2.	Cài đặt Scrapy-Splash
Để sử dụng scrapy ta có thể cài đặt qua lệnh:
$ pip install scrapy scrapy-splash
3.	Sử dụng Scrappy-Splash
Source code của công cụ được đăng tải tại: https://github.com/locth/scrappy_crawl
Công cụ này được viết ra chuyên để thu thập video từ website xnxx.com. Đây là một website đã bị chặn tại Việt Nam. Tuy nhiên, người sử dụng vẫn có thể sử dụng một số công cụ VPN để truy cập vào website này. Do đó, nếu không thể truy cập vào website trên bằng cách thông thường, vui lòng sử dụng VPN để truy cập để có thể chạy được công cụ do máy tính phải truy cập được vào website thì mới khả năng thu thập dữ liệu.
Để có thể chạy được công cụ, trước hết, cần phải chạy Docker đã được hướng dẫn tại mục 2.1. Tiếp theo, di chuyển tới thư mục tut:
$ cd tut
Tại thư mục này, chạy lệnh:
$ scrapy crawl vid
Lúc này, hệ thống sẽ quét qua toàn bộ website thông qua URL https://www.xnxx.com/video-vmyi95d/gorgeous_young_girl_sucks_dick_like_a_pornstar_-_natalissa được định nghĩa trong source code (có thể thay đổi URL để crawl trên một trang có chứa video khác cũng thuộc xnxx). Tại website này, scrapy sẽ tìm và trích xuất ra nguồn của website bằng cách sử dụng xpath "//script[contains(.,' html5player.setVideoHLS')]".
Khi có được link nguồn của video, ta có thể dễ dàng tải được video từ website này.
