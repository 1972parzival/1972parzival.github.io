import Image from 'next/image';
import Link from 'next/link';
import { getVisibleAutomatedCategories } from '@/lib/posts';
import { getCategoryByName } from '@/lib/categories';

function categoryToSlug(categoryName: string): string {
  return categoryName
    .toLowerCase()
    .replace(/\s+/g, '-')
    .replace(/[&]/g, '')
    .replace(/[^a-z0-9-]/g, '');
}

export default async function Home() {
  const categories = await getVisibleAutomatedCategories();
  return (
    <>
      {/* Hero Section */}
      <section data-bs-version="5.1" className="header14 cid-sFzxmVl7J6 mbr-bg-black" id="header14-1f">
        <div className="container">
          <div className="row justify-content-center align-items-center">
            <div className="col-12 col-md-6 image-wrapper">
              <Image 
                src="/assets/images/snap-973x1006.jpg" 
                alt="Archie Haddley Morris"
                width={973}
                height={1006}
                priority
              />
            </div>
            <div className="col-12 col-md">
              <div className="text-wrapper">
                <h1 className="mbr-section-title mbr-fonts-style mb-3 display-1 mbr-white">
                  <strong>Archie </strong><br/><strong>Haddley Morris</strong>
                </h1>
                <p className="mbr-text mbr-fonts-style display-7 mbr-white">
                  This is my website for showcasing some of the projects I work on and services I provide.
                </p>
                <div className="mbr-section-btn mt-3">
                  <Link href="/posts/contact" className="btn btn-primary display-4">
                    Contact Me
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Categories Section */}
      <section data-bs-version="5.1" className="features1 cid-sFzyUE9AaP mbr-bg-black" id="features1-1i">
        <div className="container">
          <div className="row mb-5">
            <div className="col-12 text-center">
              <h3 className="mbr-section-title mbr-fonts-style mb-4 display-2 mbr-white">
                <strong>Browse by Category</strong>
              </h3>
              <div className="d-flex flex-wrap justify-content-center gap-2">
                {categories.map((category) => {
                  const categoryData = getCategoryByName(category);
                  const slug = categoryData ? categoryData.slug : categoryToSlug(category);
                  return (
                    <Link
                      key={category}
                      href={`/posts/category/${slug}`}
                      className="btn btn-sm btn-outline-primary mbr-fonts-style display-7"
                    >
                      {categoryData?.icon || '📄'} {category}
                    </Link>
                  );
                })}
              </div>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}