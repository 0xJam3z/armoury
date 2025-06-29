#Maintainer: Viking @Vikingfr <https://twitter.com/Vikingfr>
#Maintainer: Mayfly @M4yFly <https://twitter.com/M4yFly>
#Maintainer: Erick Sanchez Vera "T1erno" <erickdeveloper2000@outlook com>

pkgname=armoury
pkgver=1.2.7
pkgrel=1
pkgdesc='Armoury is just a quick inventory and launcher for hacking programs'
url='https://github.com/0xJam3z/armoury'
arch=('any')
license=('GPL-3.0')
depends=('python' 'python-pip')
makedepends=('git')
source=(${pkgname}::git+https://github.com/0xJam3z/armoury.git)
sha256sums=('SKIP')

build() {
	cd $pkgname
	python setup.py build
}

package() {
	cd "$srcdir/$pkgname"
	python setup.py install --root="$pkgdir/" --optimize=1
	mkdir -p "$pkgdir/usr/bin"
	ln -s /usr/bin/armoury "$pkgdir/usr/bin/a"
	echo "alias a='armoury'" >> ~/.bash_aliases
	echo "alias a='armoury'" >> ~/.zshrc
	echo "alias a='armoury'" >> ~/.bashrc
}
