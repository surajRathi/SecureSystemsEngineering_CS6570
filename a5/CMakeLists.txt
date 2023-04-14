cmake_minimum_required(VERSION 3.5)
project(a5 C)

set(CMAKE_C_STANDARD 11)

#set(OPENSSL_USE_STATIC_LIBS TRUE)
find_package(OpenSSL REQUIRED)

#add_executable(a5 main.c)

#add_executable(a5_s main.c)
#target_link_options(a5_s PRIVATE -static-libgcc -static-libstdc++ -static)
#target_link_options(a5_s PRIVATE -static-libgcc -static)

add_executable(double_hash hash_generator.c)
target_link_libraries(double_hash OpenSSL::SSL)

add_executable(hash_executer hash_executer.c)
target_link_libraries(hash_executer OpenSSL::SSL)