#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RcppGSL
Version  : 0.3.8
Release  : 4
URL      : https://cran.r-project.org/src/contrib/RcppGSL_0.3.8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RcppGSL_0.3.8.tar.gz
Summary  : 'Rcpp' Integration for 'GNU GSL' Vectors and Matrices
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-RcppGSL-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : buildreq-R
BuildRequires : gsl-dev

%description
The 'GNU Scientific Library' (or 'GSL') is a collection of numerical routines for
 scientific computing. It is particularly useful for C and C++ programs as it
 provides a standard C interface to a wide range of mathematical routines. There
 are over 1000 functions in total with an extensive test suite. The 'RcppGSL'
 package provides an easy-to-use interface between 'GSL' data structures and
 R using concepts from 'Rcpp' which is itself a package that eases the
 interfaces between R and C++. This package also serves as a prime example of
 how to build a package that uses 'Rcpp' to connect to another third-party
 library. The 'autoconf' script, 'inline' plugin and example package can all
 be used as a stanza to  write a similar package against another library.

%package lib
Summary: lib components for the R-RcppGSL package.
Group: Libraries

%description lib
lib components for the R-RcppGSL package.


%prep
%setup -q -c -n RcppGSL
cd %{_builddir}/RcppGSL

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592854870

%install
export SOURCE_DATE_EPOCH=1592854870
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RcppGSL
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RcppGSL
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RcppGSL
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc RcppGSL || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RcppGSL/DESCRIPTION
/usr/lib64/R/library/RcppGSL/INDEX
/usr/lib64/R/library/RcppGSL/Meta/Rd.rds
/usr/lib64/R/library/RcppGSL/Meta/features.rds
/usr/lib64/R/library/RcppGSL/Meta/hsearch.rds
/usr/lib64/R/library/RcppGSL/Meta/links.rds
/usr/lib64/R/library/RcppGSL/Meta/nsInfo.rds
/usr/lib64/R/library/RcppGSL/Meta/package.rds
/usr/lib64/R/library/RcppGSL/Meta/vignette.rds
/usr/lib64/R/library/RcppGSL/NAMESPACE
/usr/lib64/R/library/RcppGSL/NEWS.Rd
/usr/lib64/R/library/RcppGSL/R/RcppGSL
/usr/lib64/R/library/RcppGSL/R/RcppGSL.rdb
/usr/lib64/R/library/RcppGSL/R/RcppGSL.rdx
/usr/lib64/R/library/RcppGSL/doc/RcppGSL-intro.Rnw
/usr/lib64/R/library/RcppGSL/doc/RcppGSL-intro.pdf
/usr/lib64/R/library/RcppGSL/doc/index.html
/usr/lib64/R/library/RcppGSL/examples/RcppGSLExample/DESCRIPTION
/usr/lib64/R/library/RcppGSL/examples/RcppGSLExample/NAMESPACE
/usr/lib64/R/library/RcppGSL/examples/RcppGSLExample/R/RcppExports.R
/usr/lib64/R/library/RcppGSL/examples/RcppGSLExample/R/colNorm.R
/usr/lib64/R/library/RcppGSL/examples/RcppGSLExample/configure
/usr/lib64/R/library/RcppGSL/examples/RcppGSLExample/configure.ac
/usr/lib64/R/library/RcppGSL/examples/RcppGSLExample/man/colNorm.Rd
/usr/lib64/R/library/RcppGSL/examples/RcppGSLExample/src/Makevars.in
/usr/lib64/R/library/RcppGSL/examples/RcppGSLExample/src/Makevars.win
/usr/lib64/R/library/RcppGSL/examples/RcppGSLExample/src/RcppExports.cpp
/usr/lib64/R/library/RcppGSL/examples/RcppGSLExample/src/colNorm.cpp
/usr/lib64/R/library/RcppGSL/examples/RcppGSLExample/src/colNorm_old.cpp
/usr/lib64/R/library/RcppGSL/examples/bSpline/bSpline.R
/usr/lib64/R/library/RcppGSL/examples/bSpline/bSpline.cpp
/usr/lib64/R/library/RcppGSL/help/AnIndex
/usr/lib64/R/library/RcppGSL/help/RcppGSL.rdb
/usr/lib64/R/library/RcppGSL/help/RcppGSL.rdx
/usr/lib64/R/library/RcppGSL/help/aliases.rds
/usr/lib64/R/library/RcppGSL/help/paths.rds
/usr/lib64/R/library/RcppGSL/html/00Index.html
/usr/lib64/R/library/RcppGSL/html/R.css
/usr/lib64/R/library/RcppGSL/include/RcppGSL.h
/usr/lib64/R/library/RcppGSL/include/RcppGSLForward.h
/usr/lib64/R/library/RcppGSL/include/RcppGSL_matrix.h
/usr/lib64/R/library/RcppGSL/include/RcppGSL_matrix_view.h
/usr/lib64/R/library/RcppGSL/include/RcppGSL_typedef.h
/usr/lib64/R/library/RcppGSL/include/RcppGSL_types.h
/usr/lib64/R/library/RcppGSL/include/RcppGSL_vector.h
/usr/lib64/R/library/RcppGSL/include/RcppGSL_vector_view.h
/usr/lib64/R/library/RcppGSL/skeleton/Makevars.in
/usr/lib64/R/library/RcppGSL/skeleton/Makevars.win
/usr/lib64/R/library/RcppGSL/skeleton/configure
/usr/lib64/R/library/RcppGSL/skeleton/configure.win
/usr/lib64/R/library/RcppGSL/tests/tinytest.R
/usr/lib64/R/library/RcppGSL/tinytest/cpp/gsl.cpp
/usr/lib64/R/library/RcppGSL/tinytest/test_client_package.R
/usr/lib64/R/library/RcppGSL/tinytest/test_fastLm.R
/usr/lib64/R/library/RcppGSL/tinytest/test_gsl.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RcppGSL/libs/RcppGSL.so
