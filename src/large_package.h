#pragma once

#ifdef WIN32
  #define large_package_EXPORT __declspec(dllexport)
#else
  #define large_package_EXPORT
#endif

large_package_EXPORT void large_package();
