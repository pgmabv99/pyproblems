@echo on
dir
javac  .\src\net\codejava\servlet\QuickServlet.java^
        -cp "C:\Users\alexe\source\repos\servlet\javax.servlet-api-3.0.1.jar" ^
         -d .\WebContent\WEB-INF\classes -g:source,lines,vars
         
jar cfv deploy\QuickServletApp.war -C WebContent .

copy  deploy\QuickServletApp.war C:\Users\alexe\source\repos\apache\apache-tomcat-9.0.43-windows-x64\apache-tomcat-9.0.43\webapps\.
