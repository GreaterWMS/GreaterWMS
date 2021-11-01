// Copyright 2007-2010 Baptiste Lepilleur
// Distributed under MIT license, or public domain if desired and
// recognized in your jurisdiction.
// See file LICENSE for detail or copy at http://jsoncpp.sourceforge.net/LICENSE
/*
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/
#ifndef JSONCPP_BATCHALLOCATOR_H_INCLUDED
# define JSONCPP_BATCHALLOCATOR_H_INCLUDED

# include <stdlib.h>
# include <assert.h>

# ifndef JSONCPP_DOC_EXCLUDE_IMPLEMENTATION

namespace Json {

/* Fast memory allocator.
 *
 * This memory allocator allocates memory for a batch of object (specified by
 * the page size, the number of object in each page).
 *
 * It does not allow the destruction of a single object. All the allocated objects
 * can be destroyed at once. The memory can be either released or reused for future
 * allocation.
 * 
 * The in-place new operator must be used to construct the object using the pointer
 * returned by allocate.
 */
template<typename AllocatedType
        ,const unsigned int objectPerAllocation>
class BatchAllocator
{
public:
   typedef AllocatedType Type;

   BatchAllocator( unsigned int objectsPerPage = 255 )
      : freeHead_( 0 )
      , objectsPerPage_( objectsPerPage )
   {
//      printf( "Size: %d => %s\n", sizeof(AllocatedType), typeid(AllocatedType).name() );
      assert( sizeof(AllocatedType) * objectPerAllocation >= sizeof(AllocatedType *) ); // We must be able to store a slist in the object free space.
      assert( objectsPerPage >= 16 );
      batches_ = allocateBatch( 0 );   // allocated a dummy page
      currentBatch_ = batches_;
   }

   ~BatchAllocator()
   {
      for ( BatchInfo *batch = batches_; batch;  )
      {
         BatchInfo *nextBatch = batch->next_;
         free( batch );
         batch = nextBatch;
      }
   }

   /// allocate space for an array of objectPerAllocation object.
   /// @warning it is the responsability of the caller to call objects constructors.
   AllocatedType *allocate()
   {
      if ( freeHead_ ) // returns node from free list.
      {
         AllocatedType *object = freeHead_;
         freeHead_ = *(AllocatedType **)object;
         return object;
      }
      if ( currentBatch_->used_ == currentBatch_->end_ )
      {
         currentBatch_ = currentBatch_->next_;
         while ( currentBatch_  &&  currentBatch_->used_ == currentBatch_->end_ )
            currentBatch_ = currentBatch_->next_;

         if ( !currentBatch_  ) // no free batch found, allocate a new one
         { 
            currentBatch_ = allocateBatch( objectsPerPage_ );
            currentBatch_->next_ = batches_; // insert at the head of the list
            batches_ = currentBatch_;
         }
      }
      AllocatedType *allocated = currentBatch_->used_;
      currentBatch_->used_ += objectPerAllocation;
      return allocated;
   }

   /// Release the object.
   /// @warning it is the responsability of the caller to actually destruct the object.
   void release( AllocatedType *object )
   {
      assert( object != 0 );
      *(AllocatedType **)object = freeHead_;
      freeHead_ = object;
   }

private:
   struct BatchInfo
   {
      BatchInfo *next_;
      AllocatedType *used_;
      AllocatedType *end_;
      AllocatedType buffer_[objectPerAllocation];
   };

   // disabled copy constructor and assignement operator.
   BatchAllocator( const BatchAllocator & );
   void operator =( const BatchAllocator &);

   static BatchInfo *allocateBatch( unsigned int objectsPerPage )
   {
      const unsigned int mallocSize = sizeof(BatchInfo) - sizeof(AllocatedType)* objectPerAllocation
                                + sizeof(AllocatedType) * objectPerAllocation * objectsPerPage;
      BatchInfo *batch = static_cast<BatchInfo*>( malloc( mallocSize ) );
      batch->next_ = 0;
      batch->used_ = batch->buffer_;
      batch->end_ = batch->buffer_ + objectsPerPage;
      return batch;
   }

   BatchInfo *batches_;
   BatchInfo *currentBatch_;
   /// Head of a single linked list within the allocated space of freeed object
   AllocatedType *freeHead_;
   unsigned int objectsPerPage_;
};


} // namespace Json

# endif // ifndef JSONCPP_DOC_INCLUDE_IMPLEMENTATION

#endif // JSONCPP_BATCHALLOCATOR_H_INCLUDED

