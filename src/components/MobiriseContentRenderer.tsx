'use client';

import React from 'react';
//import Image from 'next/image';

interface MobiriseContentRendererProps {
  markdownContent: string;
}

export default function MobiriseContentRenderer({ markdownContent }: MobiriseContentRendererProps) {
  return (
    <section className="content5 cid-content5 mbr-bg-black" data-bs-version="5.1">
      <div className="container">
        <div className="row justify-content-center">
          <div className="col-md-12 col-lg-10">
            <div className="mbr-text mbr-fonts-style display-7 mbr-white markdown-content">
              <div dangerouslySetInnerHTML={{ __html: markdownContent }} />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
