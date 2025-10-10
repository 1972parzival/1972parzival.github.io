import { getVisibleBlogPosts, getVisibleAutomatedCategories, BlogPost } from '@/lib/posts';
import { getCategoryByName } from '@/lib/categories';
import Link from 'next/link';
import Image from 'next/image';

function categoryToSlug(categoryName: string): string {
  return categoryName
    .toLowerCase()
    .replace(/\s+/g, '-')
    .replace(/[&]/g, '')
    .replace(/[^a-z0-9-]/g, '');
}

export default async function PostsPage() {
  const posts = await getVisibleBlogPosts();
  const categories = await getVisibleAutomatedCategories();

  return (
    <section data-bs-version="5.1" className="content2 cid-socNq9ZEoK mbr-bg-black" id="content2-q">
      <div className="container">
        {/* Statistics */}
        <div className="row mb-4">
          <div className="col-md-12 text-center">
            <p className="mbr-text mbr-fonts-style display-7 mbr-white">
              Total posts: {posts.length} | Categories: {categories.length}
            </p>
          </div>
        </div>

        {/* Breadcrumb Navigation */}
        <div className="row mt-3">
          <div className="col-12 text-center">
            <nav aria-label="breadcrumb">
              <ol className="breadcrumb justify-content-center">
                <li className="breadcrumb-item">
                  <Link href="/" className="text-primary">Home</Link>
                </li>
                <li className="breadcrumb-item active mbr-white" aria-current="page">
                  Posts
                </li>
              </ol>
            </nav>
          </div>
        </div>

        {/* Category Filter Pills - At top */}
        <div className="row mb-5">
          <div className="col-12 text-center">
            <h6 className="mbr-fonts-style display-7 mb-3 mbr-white">
              <strong>Browse by Category:</strong>
            </h6>
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

        {/* Projects - Single Continuous Grid */}
        <div className="projects-section mb-5">
          
          <div className="row">
            {posts.map((post: BlogPost) => (
              <div key={post.slug} className="item features-image col-12 col-md-6 col-lg-4 mb-4">
                <div className="item-wrapper">
                  <div className="item-img">
                    <Link href={`/posts/${post.slug}`}>
                      <Image
                        src={post.image || '/assets/images/posts-meta.svg'}
                        alt="Mobirise Website Builder"
                        width={300}
                        height={200}
                        className="img-fluid"
                      />
                    </Link>
                  </div>
                  <div className="item-content">
                    <h5 className="item-title mbr-fonts-style display-5">
                      <Link href={`/posts/${post.slug}`} className="text-primary">
                        <strong>{post.title}</strong>
                      </Link>
                    </h5>
                    <h6 className="item-subtitle mbr-fonts-style mt-1 display-7 mbr-white">
                      <strong>Archie Haddley-Morris</strong>
                      <em> • {new Date(post.date).toLocaleDateString('en-US', {
                        year: 'numeric',
                        month: 'long',
                        day: 'numeric'
                      })}</em>
                    </h6>
                    <p className="mbr-text mbr-fonts-style mt-3 display-7 mbr-white">
                      {post.description}
                    </p>
                    
                    {/* Tags */}
                    {post.tags.length > 0 && (
                      <div className="mt-2 mb-2">
                        {post.tags.slice(0, 3).map((tag) => (
                          <span
                            key={tag}
                            className="badge bg-secondary me-1"
                            style={{ fontSize: '0.75rem' }}
                          >
                            {tag}
                          </span>
                        ))}
                      </div>
                    )}
                  </div>
                  <div className="mbr-section-btn item-footer mt-2">
                    <Link href={`/posts/${post.slug}`} className="btn btn-primary item-btn display-7">
                      Read More &gt;
                    </Link>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
