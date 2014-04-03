//
//  mainViewController.h
//  Heaped
//
//  Created by Michael Zhao on 4/2/14.
//  Copyright (c) 2014 Michael Zhao. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface mainViewController : UIViewController
// Distances from beacons.
@property (strong, nonatomic) IBOutlet UILabel *distance0;
@property (strong, nonatomic) IBOutlet UILabel *distance1;
@property (strong, nonatomic) IBOutlet UILabel *distance2;

// Beacon unique identifiers?
@property (strong, nonatomic) IBOutlet UILabel *beaconID0;
@property (strong, nonatomic) IBOutlet UILabel *beaconID1;
@property (strong, nonatomic) IBOutlet UILabel *beaconID2;

// Need to show major/minor for region identification.

- (IBAction)startData:(id)sender;
- (IBAction)stopData:(id)sender;

@end
