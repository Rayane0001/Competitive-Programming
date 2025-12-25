cmake_minimum_required(VERSION 4.1)
project(Competitive)

set(CMAKE_CXX_STANDARD 14)

file(GLOB_RECURSE ALL_CPP_FILES CONFIGURE_DEPENDS "${CMAKE_SOURCE_DIR}/*.cpp")

foreach(SRC_FILE IN LISTS ALL_CPP_FILES)
    file(RELATIVE_PATH REL_SRC "${CMAKE_SOURCE_DIR}" "${SRC_FILE}")
    string(REPLACE "/" "_" TARGET_NAME "${REL_SRC}")
    string(REGEX REPLACE "\\.cpp$" "" TARGET_NAME "${TARGET_NAME}")
    add_executable(${TARGET_NAME} ${SRC_FILE}
            USACO/SpeedingTicket.cpp)
endforeach()
