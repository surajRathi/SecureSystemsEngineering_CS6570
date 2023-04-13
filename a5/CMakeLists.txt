cmake_minimum_required(VERSION 3.26)
project(a5 C)

set(CMAKE_C_STANDARD 17)

add_executable(a5 main.c)

add_executable(a5_s main.c)
#target_link_options(a5_s PRIVATE -static-libgcc -static-libstdc++ -static)
target_link_options(a5_s PRIVATE -static-libgcc -static)

add_executable(double_hash hash_generator.c)
find_package(OpenSSL REQUIRED)
target_link_libraries(double_hash OpenSSL::SSL)

add_executable(hash_executer hash_executer.c)
find_package(OpenSSL REQUIRED)
target_link_libraries(hash_executer OpenSSL::SSL)