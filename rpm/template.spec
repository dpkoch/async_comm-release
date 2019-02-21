Name:           ros-melodic-async-comm
Version:        0.1.1
Release:        0%{?dist}
Summary:        ROS async_comm package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-melodic-catkin
BuildRequires:  boost-devel
BuildRequires:  cmake

%description
A C++ library for asynchronous serial communication

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Feb 21 2019 Daniel Koch <danielpkoch@gmail.com> - 0.1.1-0
- Autogenerated by Bloom

* Tue Sep 04 2018 Daniel Koch <danielpkoch@gmail.com> - 0.1.0-0
- Autogenerated by Bloom

