#
# Conditional build:
%bcond_without	tests		# build without tests
#
Summary:	libferris is a virtual file system (VFS) that runs in the user address space
Name:		libferris
Version:	1.2.4
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/witme/%{name}-%{version}.tar.bz2
# Source0-md5:	1135799ef30677c74e1d3e4406147c96
URL:		http://witme.sourceforge.net/libferris.web/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'libferris' is a virtual filesystem that exposes hierarchical data of
all kinds through a common C++ interface. Access to data is performed
using C++ IOStreams and Extended Attributes (EA) can be attached to
each datum to present metadata. Ferris uses a plugin API to read
various data sources and expose them as contexts and to generate
interesting EA.

%prep
%setup -q

mv -f configure{,.dist}

%build
if [ ! -f configure -o configure.ac -nt configure ]; then
	%{__aclocal} -I macros
	%{__autoconf}
	%{__autoheader}
	%{__automake}
fi
%configure \
	%{?debug:--enable-vmdebug --enable-resolvedebug} \
	--enable-annodex \
	--enable-beagle \
	--enable-btparse \
	--enable-cgicc \
	--enable-clucene \
	--enable-curl \
	--enable-dbus-c++ \
	--enable-dbus-mounting \
	--enable-djvu \
	--enable-dtl \
	--enable-ecore \
	--enable-edb \
	--enable-eet \
	--enable-epeg \
	--enable-evolution \
	--enable-gcj \
	--enable-gdbm \
	--enable-gphoto2 \
	--enable-gtkextra2 \
	--enable-imagemagick \
	--enable-imlib2 \
	--enable-libbz2 \
	--enable-libexif \
	--enable-libmpeg3-support \
	--enable-libtextcat \
	--enable-libz \
	--enable-lucene \
	--enable-mysqlpp \
	--enable-obby \
	--enable-plugin-extractor \
	--enable-pqxx \
	--enable-selinux \
	--enable-sqlite3 \
	--enable-strigi \
	--enable-svmlight \
	--enable-tdb \
	--enable-xapian \
	--enable-xine \
	--enable-xmms \
%if %{without tests}
	--disable-glibtest \
	--disable-gtktest \
	--disable-xinetest \
%endif
	--with-dbxml-db4-prefix=/usr
	--with-gpgme-exec-prefix=/usr
	--with-gpgme-prefix=/usr
	--with-kde-libdir=%{_libdir}/kde3
	--with-liba52=/usr \
	--with-libattr=/usr \
	--with-libid3=/usr \
	--with-libjasper=/usr \
	--with-libjpeg=/usr \
	--with-libmpeg2=/usr \
	--with-libmpeg3=/usr \
	--with-libpng=/usr \
	--with-pccts=/usr \
	--with-qt \
	--with-swig-ocaml \
	--with-swig-perl \
	--with-swig-python-prefix=/usr
	--with-x \
	--with-xqilla=/usr \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
