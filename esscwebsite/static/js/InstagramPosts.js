import React, { useState } from 'react';

const InstagramPosts = ({ posts }) => {
  const [showCaption, setShowCaption] = useState(false);
  const [selectedCaption, setSelectedCaption] = useState('');

  const toggleCaption = (caption) => {
    setShowCaption(!showCaption);
    setSelectedCaption(caption);
  };

  return (
    <section className="page-section" id="instagram-posts">
      <div className="container">
        <div className="text-center">
          <h2 className="section-heading text-uppercase">Instagram Posts</h2>
        </div>
        <div className="row" id="instagram-posts-container">
          {posts.map((post, index) => (
            <div className="col-lg-4 col-sm-6 mb-4" key={index}>
              <div className="instagram-post">
                <img src={post.thumbnail_url} alt="Instagram Post" className="img-fluid" onClick={() => toggleCaption(post.caption)} />
                {showCaption && selectedCaption === post.caption && (
                  <p>{post.caption}</p>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default InstagramPosts;