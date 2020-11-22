import { TestBed } from '@angular/core/testing';

import { StackserviceService } from './stackservice.service';

describe('StackserviceService', () => {
  let service: StackserviceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(StackserviceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
